---
layout: page
title: Topological Quantum Field Theories
description: Topological Quantum Field Theories, specifically non-abelian Chern Simons theories, and their applications.
importance: 1
category: obsidian
---

> [!example]- _Referring to_
>
> - _[Undergraduate Lecture Notes in Topological Quantum Field Theory](http://arXiv.org/abs/0810.0344v5) by Vladimir G. Ivancevic, Tijana T. Ivancevic_[^1]
> - _Topological Quantum Field Theories – A Meeting Ground for Physicists and Mathematicians by Romesh Kaul_[^2]
> - _Introduction To Chern-Simons Theories by Gregory W. Moore_[^5]
> - _Quantum Field Theory on the Plane by David Tong_[^6]

### Recaps

Recap of [[Physics/Time Evolution Pictures|the 3 pictures of time evolution in QM]] and [[Physics/Perturbation Theory|perturbation theory using the Dirac picture]] in the context of [[S-Matrix Formalism|transition probabilities]].
Recap [[Axiomatic Quantum Mechanics|quantum mechanical phase space]] and [[Quantum Field Theory]].
Recap [[Gauge Theories|gauge theories]], [[Differential Forms|differential forms]] and the [[Physics/Action Formulation|action formulation]].
Recap [[Spontaneous Symmetry Breaking|Higgs Mechanism]].
Recap [[Path Integral Formulation]], [[Wick Rotations]], [[Correlation Functions]], [[Quantum Electrodynamics]], [[Partition Function]], [[Faddeev-Popov Trick and Ghosts]].
Related and interesting is [[Planar QFT]].

### Introduction

What are TQFTs?

> Toplogical quantum field theories are independent of the metric of curved manifold on which these are defined; the expectation value of the energy-momentum tensor is zero, $⟨T_{μν}⟩ = 0$. _These possess no local propagating degrees of freedom; only degrees of freedom are topological._ Operators of interest in such a theory are also metric independent.

They have the interesting feature of being exactly solvable, no perturbation needed.

#### Motivation from [[Knot Theory]]

Knot theory is concerned with the topological equivalence of knots and links. TQFTs arise from considering theories which provide such a description of the knots and links embedded in that space - so we want the observables over the knots to be metric independent.

# Path Integral TQFT

Considering fields $\phi_i$ on a manifold $M$ with metric $g_{\mu\nu}$, with an action $S[\phi_i]$ and some operators $\mathcal O_\alpha$ defined, we have vacuum expectation values defined as

$$
\langle \mathcal O _{\alpha} \rangle = \int D[\phi_i] \mathcal O_\alpha(\phi_i) e^{\iota S[\phi_i]}
$$

^7f47b8

If the vacuum expectation values of some selected operators and their products remain invariant under changes to the metric, the field theory is considered **topological** and these operators the _observables_.

$$
\frac{\delta}{\delta g_{\mu\nu}} \langle \mathcal O_{\alpha_1}\dots\mathcal O_{\alpha_n}\rangle =0
$$

**Schwarz-type** TQFTs guarantee this formally by requiring $S,\mathcal O_\alpha$ to be metric-independent. An example, which I will cover in detail along with its relation to knot theory, is the following:

## [[Chern-Simons Gauge Theory|Chern-Simons Gauge Theory]]

Composed of

- A differentiable, compact 3-manifold $M$
- A simple, compact gauge group $G$ (with corresponding gauge [[Differential Geometry#^eb1faf|connection]] $A$) (refer to [[Gauge Theories#^199c52|gauge theories]])
- Integer parameter $k$ (required to be integral for gauge invariance)
  Then we have a Chern-Simons form, which integrates to give the action:
  $$
  S_{CS}[A] = \int _M\text{Tr}(A\wedge dA +\frac 23 A\wedge A\wedge A)
  $$

## Witten-type TQFTs

The second way to ensure metric invariance of the action and observables, and also called cohomological of Witten–type.
We require a symmetry with the infinitesimal transformation $\delta'$:

$$
\begin{align}\delta' \mathcal O_\alpha(\phi_i) &= 0\\ T_{\mu\nu}(\phi_i) &=\delta' G_{\mu\nu} (\phi_i)\\
\text{Where }T_{\mu\nu} (\phi_i)&\equiv  \frac{\delta }{\delta g_{\mu\nu} }S[\phi_i] \end{align}
$$

Note here $G_{\mu\nu}$ is some arbitrary tensor.
Since $\delta'$ is a symmetry, $\delta' S=0$ and $\delta' \mathcal O_\alpha(\phi_i)=0$ under transformations $\delta' \phi_i$.
Looking again at the vacuum expectation values,

$$
\begin{gather}
\frac{\delta}{\delta g_{\mu\nu}}\langle \mathcal O_{\alpha_1}\dots\mathcal O_{\alpha_n}\rangle = i\int D[\phi_i] \mathcal O_{\alpha_1}(\phi_i)\dots\mathcal O_{\alpha_n}(\phi_i) e^{\iota S[\phi_i]} T_{\mu\nu}(\phi_i)\\
= \delta'\left(i\int D[\phi_i]  \mathcal O_{\alpha_1}(\phi_i)\dots\mathcal O_{\alpha_n}(\phi_i) G_{\mu\nu}(\phi_i) e^{\iota S[\phi_i]}\right)\\
=0
\end{gather}
$$

Since an expectation value will not change under symmetry transformations, the final equality holds. We have also implicitly assumed the measure is invariant under the transformation.
Note that the operators have been assumed metric-independent in the above proof, but it can be extended more generally to $\frac{\delta}{\delta g_{\mu\nu}} \mathcal O_\alpha(\phi_i) = \delta' O_\alpha^{\mu\nu} (\phi_i)$, where we have defined additional arbitrary tensor functionals.

$\delta'$ must also be a scalar symmetry, since it is a global symmetry and so has a constant parameter corresponding - if that were not a scalar, it would be a pretty harsh constraint to be satisfied on arbitrary manifolds.

Often, cohomological TQFTs satisfy $S=\delta' \Lambda$, which allows showing that any combination of observables is independent of the coupling constant, appearing in the theory as $\exp\left( \iota\frac 1 {g^2} S\right)$. A proof to first-order is given in the reference, simply take $1/g^2\rightarrow1/g^2-\Delta$, assume the observables' form doesn't depend on the coupling, and a similar proof to the one for VEVs follows.

## Hodge Decomposition Theorem

Recap [[Differential Forms]], specifically the [[Differential Forms#Hodge Operator|Hodge Operator]].
The Hodge Star operator $*:\Lambda^p(M)\rightarrow\Lambda^{n-p}(M)$ maps $p$-forms to their dual $n-p$ forms, and is generally defined with respect to an inner product, so that it has the properties (where $\mu$ is the canonical volume $n$-form):$$\begin{gather}\alpha\wedge *\beta = \beta\wedge *\alpha= \langle \alpha,\beta\rangle\mu\\**\alpha = (-1)^{p(n-p)}\alpha\end{gather}$$Alternatively, for any two $p$-forms with compact support on $M$, the Hodge star can be used to define a bilinear and positive definite $L^2$ inner product:$$\langle \alpha,\beta\rangle = \int_M \alpha\wedge *\beta $$

### Codifferential

> [!def] Definition : Codifferential
> The formal adjoint (aka Hodge dual) of the exterior derivative $d:\Lambda^p(M)\rightarrow\Lambda^{p+1}(M)$ is the map $\delta:\Lambda^p(M)\rightarrow\Lambda^{p-1}(M)$, a generalisation of the divergence, defined as$$\delta = (-1)^{n(p+1)+1}*d* \Leftrightarrow d = (-1)^{np}*\delta*$$
> Essentially the dual of the derivative of the dual of a $p$-form, up to a sign. On an even-dim manifold, the sign is always $-1$.

- $\delta$ of a 0-form is 0.
- If $\alpha=d\beta$, $\beta$ is the _exact_ form of $\alpha$. If $\alpha=\delta\beta$, $\beta$ is the _coexact_ form of $\alpha$.
- $\alpha$ is _closed_ if $d\alpha=0$, and it is $coclosed$ if $\delta\alpha=0$ - in which case $*\alpha$ is closed.
- $d^2=0$ and $\delta^2=0$
- $\delta*=(-1)^{p+1}*d,\quad *\delta=(-1)^p*d$
- $d\delta * = *\delta d,\quad*d\delta=\delta d*$

> [!def] Definition : Hodge Laplacian
> Defined by coupling the co-differential to the exterior derivative, $$\begin{gather}\Delta:\Lambda^p(M)\rightarrow\Lambda^p(M)\\\Delta = \delta d+d\delta = (d+\delta)^2\end{gather}$$
> Properties:
>
> - $[\delta,\Delta]=[d,\Delta]=[*,\Delta]=0$
> - $\delta\Delta=\delta d\delta$
> - $d\Delta = d\delta d$

A $p$ form is called a harmonic if $\Delta\alpha=0$.

> [!tip] Proposition : A form is harmonic iff it is closed and coclosed.
> Proof of the forward implication:
>
> $$
> \begin{gather}
> \Delta\alpha=0\implies \alpha\wedge*\Delta\alpha=0\implies\langle\alpha,\Delta\alpha\rangle=0
> \\\langle\alpha,\Delta\alpha\rangle = \langle\alpha,d\delta\alpha \rangle+\langle\alpha,\delta d\alpha\rangle = \langle\delta\alpha,\delta\alpha\rangle+\langle d\alpha, d\alpha\rangle\end{gather}
> $$
>
> Since the norm is positive-definite, $\langle\delta\alpha,\delta\alpha\rangle$ and $\langle d\alpha,d\alpha\rangle$ must vanish separately. Hence proved.
> The converse, $d\alpha=\delta\alpha=0\implies\Delta\alpha=0$, is trivial.

### The theorem itself

---

#ST4 #Lectures

# ST4 Lectures

<div class="labelled_rule" data-content="Lecture 1" />
</div>
Let us begin with QED examples highlighting some important ideas used in TQFTs.

### Vector Potential

Also known as the connection, which is Lie algebra-valued, appears in the action, which is exponentiated to obtain a Lie group-valued path integral.
In QED, we use the vector as a one-form, and its exterior derivative is the field strength tensor (two-form): $F=\d A$. (_Sidenote_, this implies $\d F=0$ whenever $F$ can be written in terms of $A$ - though there exist effective systems where no such $A$ exists.)

## Aharanov-Bohm Effect

This describes the effect of a non-zero 4-potential on a charged particle moving through a region where the $E,B$ fields are 0, and is considered by some as the only direct proof of the gauge principle. The Maxwell equations can fundamentally not predict this - this only arises from the path integral formulation of electromagnetism.
The simplest example is to insert an infinitely-long solenoid (exactly) between the two slits in an electron interference experiment (YDSE). While the $B$ field is zero outside the solenoid, the vector potential curls around it. The path integral sums over all the paths the electron takes, and the action includes the electron coupling to $A$:

$$
P\simeq\int _\gamma e^{\iota A}
$$

Thus the two paths going through the two slits pick up opposing phases - in the path integral, these cancel, and the interference pattern should vanish with the introduction of this solenoid. And guess what. It does! See the wiki page for links to various experiments and their reviews.

Since the connection is a 1-form (and so is $e^{\iota A}$), it can be integrated over a path in 3D. Consider an electron travelling one path to the screen, $\gamma_1$, and its reflected path $\gamma_2$, then $\gamma=\gamma_1\cdot \gamma_2^{-1}$ is a closed loop. The integral over this closed loop (or any closed loop) is called a Wilson loop.

In this case, it should be clear that the Wilson loop evaluates to a non-zero value, which is also unusual - this is a _non-trivial holonomy_.
This is the effect of the changed topology of the space - excluding the solenoid from $\R^3$ gives us a solid torus instead, and the loop around this exclusion cannot be smoothly contracted to a point, hence the non-trivial holonomy.

## Cohomology Groups

Let $C^k$ be the space of all $k$ forms on a manifold $M$,

$$
\begin{gather}
C^{k-1}\xrightarrow \d C^k \xrightarrow\d C^{k+1}\\
\d^2=0\implies \Im \d_{k-1\rightarrow k} \subseteq \ker \d_{k\rightarrow k+1}
\end{gather}
$$

Note that in 3-space this means that the divergence of curl is 0.

$$
\begin{gather}
W\subseteq V\implies V/W \cong \{ v+W:v\in V\}\text{ is the quotient space.}\\
\ker \d_{k\rightarrow k+1} /\Im \d_{k-1\rightarrow k} \equiv H^k(M)
\end{gather}
$$

This is known as the $k^\text{th}$ cohomology group of the manifold. When $H^k(M)=0$, then any closed $k$-form $F$ on the manifold is exact (note that exact k-forms are always closed but the converse is not guaranteed).

```
<< Not noted: Some discussion on the Poincare conjecture, Emmy Noether's algebraic complex, and why the homology ideas we're using exist.
How do you prove that two manifolds are the same? This can be proved by showing they have the same fundamental groups. Poincare also argued that two manifolds are the same if they have the same homology groups, but later proved himself wrong with what is called the Poincare manifold. >>
```

<div class="labelled_rule" data-content="Lecture 2" />
</div>
Discussed [[Knot Theory]], Reidmeister moves, tri-colouring invariant, the Jones polynomial, and how performing surgery on knots in $\R^3$ can give us all possible 3-manifolds.
<div class="labelled_rule" data-content="Lecture 2.5" />
</div>
[Some References](https://mathoverflow.net/questions/359/a-reading-list-for-topological-quantum-field-theory)
The fundamental object in TQFTs is the path integral, which is an ill-defined object and a mathematician's worst nightmare.

> [!remark] Philosophy of TQFTs
> Topological amplitudes are computable in many cases and they produce topological invariants.
> We will not default to the path integral, but introduce amplitudes which have behaviour as if arising from a quantum field theory, and produce topological invariants.

Refer to [[Knot Theory]] for definitions of knots and knot invariants.

> [!def] TQFT
> A QFT where observables are topological invariants. These observables are called amplitudes (a path-integral terminology) but no path integrals are involved in the definition.

Using the properties of knots, we will construct an algebra which mimics the behaviours of amplitudes from path integrals, and define a TQFT rigorously.

<div class="labelled_rule" data-content="Lecture 3" /></div>

Recall parallel transport of tangent vectors on a curved manifold. This can be extended to any vector bundle (keep a copy of a vector space, eg a Hilbert space, at every point in the manifold). The trivial bundle is $M\times\mathcal H$.
Given a gauge Lie group which acts on the Hilbert space, we define the connection for that group, $A$, a Lie-algebra-valued field. The holonomy $\oint_\gamma A$ is Lie-algebra-valued, and so the phase term $e^{\iota\oint_\gamma A}$ is a Lie group element.

### References

[^1]: Ivancevic, Vladimir G., and Tijana T. Ivancevic. ‘Undergraduate Lecture Notes in Topological Quantum Field Theory’. arXiv, 10 December 2008. [http://arxiv.org/abs/0810.0344](http://arxiv.org/abs/0810.0344).

[^2]: Kaul, R. K. ‘Topological Quantum Field Theories -- A Meeting Ground for Physicists and Mathematicians’. arXiv, 15 July 1999. [https://doi.org/10.48550/arXiv.hep-th/9907119](https://doi.org/10.48550/arXiv.hep-th/9907119).

[^3]: R.K. Kaul and R. Rajaraman: Phys. Letts. B249 (1990) 433-437.

[^4]: R.K. Kaul: Complete solution of SU(2) Chern-Simons theory, hep-th/9212129; and Commun. Math. Phys. 162 (1994) 289 (hep-th/930532). https://arxiv.org/abs/hep-th/9212129

[^5]: Moore, Gregory W. ‘Introduction To Chern-Simons Theories’, n.d.

[^6]: Tong, David. Quantum Field Theory on the Plane. Lecture Notes: Gauge Theory, 8.3. https://www.damtp.cam.ac.uk/user/tong/gaugetheory/83d.pdf
