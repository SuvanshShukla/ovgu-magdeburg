import torch
from torch import nn


class HiddenLinear(nn.Module):
    def __init__(self,
                 out_units: int,
                 activation: type[nn.Module] = nn.Mish):
        """Fully connected layer with batchnorm and activation function.
        
        Parameters:
            out_units: Number of output units. Note that input units does not need to be specified due to usage of
                       LazyLinear.
            activation: Activation function, see note in CNN class.
        """
        super().__init__()
        self.linear = nn.LazyLinear(out_units, bias=False)
        self.norm = nn.BatchNorm1d(out_units)
        self.activation = activation()

    def forward(self,
                inputs: torch.Tensor) -> torch.Tensor:
        return self.activation(self.norm(self.linear(inputs)))
    

class ResidualBlockTBD(nn.Module):
    def __init__(self,
                 in_channels: int,
                 out_channels: int,
                 kernel_size: int,
                 stride: int,
                 activation: type[nn.Module] = nn.Mish,
                 padding_mode: str = "zeros"):
        """Turn this into a residual block!
        
        Parameters:
            in_channels: Number of channels in the input to this layer. NOTE that we could also use LazyConv2d and not
                         specify this. In general, it's better to be explicit and not use lazy layers. We make an
                         exception for linear layers, as computing the number of inputs can be cumbersome in case the
                         linear layer follows after a CNN stack and Flatten().
            out_channels: Number of desired output channels.
            kernel_size: Size of the convolutional filter.
            activation: Activation function, see note in CNN class.
            padding_mode: What kind of padding to use at the edges; see Conv2d docs.
        """
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size, stride,
                              bias=False, padding="same", padding_mode=padding_mode)
        self.norm1 = nn.BatchNorm2d(out_channels)
        self.activation1 = activation()
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size, stride=1,
                              bias=False, padding="same", padding_mode=padding_mode)
        self.norm2 = nn.BatchNorm2d(out_channels)
        self.activation2 = activation()

    def forward(self,
                inputs: torch.Tensor) -> torch.Tensor:
        layer1 = self.activation1(self.norm1(self.conv1(inputs)))
        return self.activation2(self.norm2(self.conv2(layer1)))


class ResNetLevelTBD(nn.Module):
    def __init__(self,
                 n_layers: int,
                 in_channels: int,
                 out_channels: int,
                 kernel_size: int,
                 stride: int,
                 activation: type[nn.Module] = nn.Mish,
                 **kwargs):
        """A sequence of residual blocks working at the same resolution & number of channels.

        All convolutions return the same resolution number of filters.
        
        Parameters:
            n_layers: How many convolution layers to apply. Pooling is extra.
            in_channels: Number of channels in the input to the first layer.
            out_channels: Number of desired output channels for each convolution.
            kernel_size: Size of all convolutional filters.
            activation: Activation function, see note in CNN class.
        """
        super().__init__()
        self.layers = nn.Sequential()
        for ind in range(n_layers):
            self.layers.append(ResidualBlockTBD(in_channels if ind == 0 else out_channels, out_channels, kernel_size,
                                                stride if ind== 0 else 1, activation, **kwargs))

    def forward(self,
                inputs: torch.Tensor) -> torch.Tensor:
        return self.layers(inputs)


class ResNetTBD(nn.Module):
    def __init__(self,
                 n_levels: int,
                 layers_per_level: int,
                 in_channels: int,
                 base_channels: int,
                 kernel_size: int,
                 n_outputs: int,
                 stride: int,
                 activation: type[nn.Module] = nn.Mish,
                 channel_max: int = 512,
                 **kwargs):
        """Wrapper for a full CNN with multiple "levels" and a final classification "head".
        
        Parameters:
            n_levels: How many levels to use. Each "level" works at one resolution, with a factor-2 pooling at the end.
                      You likely don't want to go further than a 4x4 resolution, or maybe even 8x8. For 32x32 images
                      like CIFAR, this would imply four levels at most: 32 -> 16 -> 8 -> 4 pixels.
            layers_per_level: How many convolutional layers to use at each resolution.
            in_channels: Number of channels in the input, e.g. 3 for RGB color images, or 1 for grayscale.
            base_channels: Number of channels in first level. This number is doubled for each subsequent level, up to
                           channel_max.
            kernel_size: Used for convolutions.
            n_outputs: Number of classes for the final layer.
            n_fc_layers: Use this many fully-connected hidden layers after the CNN stack, but excluding the final
                         classification layer.
            fc_units: How many units to use in the FC layers. Ignored if n_fc_layers is 0.
            activation: Activation function used throughout the network. Must be an nn.Module class, i.e. pass things
                        like nn.ReLU, NOT nn.ReLU()!
            channel_max: Will never use more than this many channels, i.e. stop doubling per level at this point.
            global_pool: If True, use global average pooling at the end of the CNN stack instead of just flattening
                         everything.
            kwargs: Further arguments to ConvLayer, e.g. padding_mode.
        """
        super().__init__()
        self.conv = nn.Conv2d(in_channels, base_channels, kernel_size, stride, padding=1)
        self.body = nn.Sequential()
        current_filters = base_channels
        previous_filters = in_channels
        
        for _ in range(n_levels):
            self.body.append(ResNetLevelTBD(layers_per_level // 2, previous_filters, current_filters,
                                            kernel_size,
                                            stride if _ != 0 else 1,
                                            activation, **kwargs))
            previous_filters = current_filters
            current_filters *= 2
            if current_filters > channel_max:
                current_filters = channel_max

        self.head = nn.Sequential(nn.AdaptiveAvgPool2d(1))
        self.head.append(nn.Flatten())
        self.head.append(nn.LazyLinear(n_outputs))

    def forward(self,
                inputs: torch.Tensor) -> torch.Tensor:
        return self.head(self.body(self.conv(inputs)))
