# Hints for Latex Syntax

[Link to render Latex online](https://quicklatex.com/)

>[!IMPORTANT]
> Remember to always start and end latex with `$` symbol in markdown

## Hat/cap symbol

```latex
$\hat{y}$
```

It looks like this: $\hat{\mu}$

## Super or Subscript

```latex
$A_{ij}^{ij}$
```

Is rendered as: $A_{ij}^{ij}$

## Symbols

An interesting thing about symbols in VIM/NVIM is that you can enter them as "digraphs".  
To know more about these "digraphs" use the `:digraph` command to view a list.  
Then use this combo to enter the symbol you want: `Ctrl+k` `{char sequence 1} {char sequence 2}`.  

For example, I to enter ∆ I did - `Ctrl+k` followed by it's code `DE`. Careful! It is case sensitive.
Checkout vim related commands here: [[useful-vimnvim-commands#Using non-latex symbols in VIM/nvim]]

| Symobl     | syntax |
| ---------- | ------ |
| Sigma      | \sigma |
| Sum simbol | \sum   |
| mew symbol | \mu    |
| partial derivative symbol | \partial |
| for all    | \forall |
| infinity   | \infty |
| logical And | \wedge |
| logical Or | \vee |
| exists     | \exists |
| element of/ in | \in |

## Example of using $\sum$

```latex
$\sum_{n=1}^{\infty} 2^{-n} = 1$
```

That is equivalent to: $\sum_{n=1}^{\infty} 2^{-n} = 1$

## Matrix

You use the `\begin{pmatrix}` & `\end{pmatrix}` markup. Like this:

```latex
$\begin{pmatrix}   1 & 2 & 3\\   a & b & c   \end{pmatrix}$
```

Here's how it would render:

$P(c) = M(n_1,n_2|p_1,p_2) := \begin{pmatrix} n_1 + n_2 \\ n_1,n_2 \end{pmatrix}.p_1^{n_1}.p_{2}^{n_2}$

**Note how `\\` is used to break lines!**

[Overleaf matrix latex documentation Link](https://www.overleaf.com/learn/latex/Matrices#amsmath_matrix_environments)

## Large brackets

use `\left(` and `\right)`

```latex
$\left(\frac{N_i}{N}\right)$
```

Here's how it looks like:

$\left(\frac{N_i}{N}\right)$

You can make them even bigger by using `\Big{` or `\Bigg`

## Empty space between words in a math equation

Simply end the word with `\`

```latex
$Gain\ Ratio = \frac{Information\ Gain}{Intrinsic\ Information}$
```

Here's what that would look like:

$Gain\ Ratio = \frac{Information\ Gain}{Intrinsic\ Information}$

## Writing cases

Useful when you want to write outcomes for something like a step-function.

Here's how you would do something like that:

```latex
f(x) = \begin{cases} x & \text{if } x > 0 \\ \alpha x & \text{if } x \le 0 \end{cases}
```

It looks like this rendered:

$$
f(x) = \begin{cases} x & \text{if } x > 0 \\ \alpha x & \text{if } x \le 0 \end{cases}
$$

