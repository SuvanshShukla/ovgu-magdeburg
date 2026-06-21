# Chapter 12 Attention Mechanism

1. What is the difference between transfer learning and fine tuning? Is one a sub-type of the other?
2. When transformers “transform” input vectors into output vectors in a new space, how exactly are the output vectors “richer”?
3. What happens if dimension of output vector is not equal to the dimension of input vector? Do we still get some output? Are the number of layers reduced? Can the layers no longer stack? (isn’t it possible for the output to be shorter/longer than the input?)
4. How does Y = Softmax[QK^T]V capture asymmetry?
5. In (the book’s) section 12.1.4 Network Parameters, how are biases being absorbed by weights (via extra row & column)?
6. How are multiplicative relations between activation values different for transformers compared to standard neural networks?
7. In (the book’s) section 12.1.7 Transform Layers, Why do we need MLP for non-linearity? How was linearity lost anyway?
8. In (the book’s) section 12.1.8 Computational Complexity, how is adding position to vectors to token vectors mathematically feasible? Aren’t they completely different quantities?
9. In (the book’s) section 12.1.9 Positional Encoding, how do we read/comprehend figure 12.10? 

## Further Questions

1. In section 12.2.3 Bag of Words, what is "loss of generality" here?
2. In section 12.2.4 Autoregressive models, How exactly does window size (L) grow exponentially? Aren't we only multiplying probabilities? I'm having trouble visualizing this. Can't we just use the base probability distribution table for further calculations?
3. In section 12.3.1 Decoder transformers (2nd paragraph), I am confused by the phrasing - "The model takes as input a sequence consisting of the first n −1 tokens, and
its corresponding output represents the conditional distribution for token n.". How does this sequence get sampled and extended?
4. In section 12.3.1 Decoder transformers, is the dimensionality of the output (D) something specified by the user? Is it inherent to the architecture? How are the dimensions chosen?
5. In section 12.3.2 Sampling strategies, I don't understand how beam search works. It's explanation was too complicated for me.
6. In section 12.3.2 Sampling strategies, Is drift necessarily bad? Doesn't that mean the model may be able to generate novel sequences?
7. In section 12.3.3 Encoder transformers, Is BERT basically a "general" encoder, able to be fine-tuned for any specialized dataset? How is this possible? Has BERT learned to encode anything?
8. In section 12.3.5 Large Language Models, Is LoRA basically adding new weights to pre-existing weights for every layer after fine-tuning?
9. In section 12.3.5 Large Language Models, Is the requirement of fine-tuning diminished for LLMs, because they can learn more niche things from large datasets by themselves? Was this intended or a side-effect?
10. In section 12.4.2 Generative image transformers, How does a conditional distribution learn that a pixel might be black or white, while a regression model might learn it should be grey. This example mentioned in the book confused me.
11. In section 12.4.4 text-to-speech, how come feeding unrelated speech alongside text to the encode works? How is this possible?
12. In section 12.4.5 vision & language transformers, Unlike for text-to-speech where input (before transformers) was a combination of text & speech, here input to decoder (after transformers) is text + image? Can decoder accept input of different modalities?
