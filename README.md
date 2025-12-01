# Impact of Alzheimer’s Pathology on Schaffer Collateral Plasticity

This computational model visualizes the fundamental mechanisms of synaptic plasticity that underlie learning and memory, comparing a healthy human hippocampus against one affected by Alzheimer's Disease (AD). [cite_start]It links the foundational "molecular logic" of memory discovered in model organisms like *Aplysia* (Kandel, 2001) to the specific pathology investigated in our research question: whether therapeutic targeting can restore synaptic stability in the face of AD.

The **x-axis represents Time (s)**, and the **y-axis represents Synaptic Weight**, a proxy for connection strength between CA3 and CA1 neurons in the Schaffer collateral pathway.

### 1. Healthy Control (Solid Blue Line)
The blue line demonstrates the functional "balance between LTP and LTD" required for healthy cognitive function:
* **LTP Induction (40-45s):** High-frequency stimulation triggers a rapid, robust increase in synaptic weight. This models the successful "insertion of new AMPA receptors" and protein phosphorylation that encodes memories (Bliss & Lomo, 1973).
* **LTD Induction (100-105s):** Low-frequency stimulation causes a controlled decrease in weight, allowing the circuit to "update and forget" information efficiently (Dudek & Bear, 1992).

### 2. Alzheimer's Disease Model (Dashed Red Line)
The red dashed line illustrates the systems-level cause of pathology described in our summary:
* **Failed LTP (40-45s):** During the same high-frequency stimulation, the synaptic weight fails to rise significantly. [cite_start]This visualizes how AD "physically disrupt[s] synaptic connections via amyloid-beta plaques". [cite_start]The presence of amyloid-beta impairs the LTP mechanism, meaning the "strong signals" from CA3 cannot be effectively strengthened at the CA1 synapse[cite: 34].
* **Synaptic Instability:** Because the synapse cannot undergo potentiation (strengthening), the circuit loses its ability to encode new long-term memories. [cite_start]This supports our research focus on finding targets to "slow down or stop the early effects" of this disruption[cite: 81].

### Conclusion
By overlaying these two conditions, the model highlights that memory loss in Alzheimer's is not just a passive decay, but an active failure of the synaptic plasticity mechanisms (LTP) that are evolutionarily conserved from simple organisms like *Aplysia* to humans

---
### Citations
Bliss, T. V. P., & Lømo, T. (1973). Long-lasting potentiation of synaptic transmission in the dentate area of the anaesthetized rabbit following stimulation of the perforant path. *Journal of Physiology*.

Dudek, S. M., & Bear, M. F. (1992). Homosynaptic long-term depression in area CA1 of hippocampus and effects of N-methyl-D-aspartate receptor blockade. *Proceedings of the National Academy of Sciences*.

Kandel, E. R. (2001). The molecular biology of memory storage: A dialogue between genes and synapses. *Science*.
