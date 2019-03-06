import numpy as np
###############################################################################
########### U-238 resonance parameters for first resonance ####################
################################################################################
a_U238 = 9.480000e-4 # (10-12 cm)
ρ0_U238 = 0.002196807122623*0.5
ρ0 = ρ0_U238
## VLAD's VALUES
μ_E0_U238 = 6.674280
μ_Γn_U238 = 1.492300e-3
μ_Γγ_U238 = 2.271100e-2
μ_Γ_U238 = np.array([μ_E0_U238, μ_Γn_U238, μ_Γγ_U238])

# CHANGE COV WHEN VLAD GIVES
cov_Γ_U238 = 100*np.diag([ 0.065126369275825552667027773401338945901507564256784,
                        0.0000060974748049746141519539917002332147619120952060896,
                        0.00000043730461508887773583171268036686758829891074351669])**2

