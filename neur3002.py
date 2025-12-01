# ==============================================================================
# 1. IMPORT LIBRARIES
# ==============================================================================
import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
# 2. DEFINE SIMULATION PARAMETERS
# ==============================================================================
def setup_parameters():
    """
    Sets up parameters for both Healthy and Alzheimer's conditions.
    """
    # Common simulation settings
    common = {
        'total_time': 150,
        'dt': 0.1,
        'hfs_start': 40,   # High-Frequency Stimulation (LTP) starts
        'hfs_end': 45,     # HFS ends
        'lfs_start': 100,  # Low-Frequency Stimulation (LTD) starts
        'lfs_end': 105,    # LFS ends
    }

    # Condition-specific settings
    conditions = {
        'Healthy': {
            'w_initial': 1.0,
            'w_max': 2.5,             # Healthy synapses can strengthen significantly
            'w_min': 0.5,
            'ltp_rate': 0.5,          # Fast learning rate
            'ltd_rate': 0.3
        },
        'Alzheimers': {
            'w_initial': 1.0,
            'w_max': 1.2,             # AD pathology prevents significant strengthening (LTP impairment)
            'w_min': 0.3,             # Synapses may weaken further/easier
            'ltp_rate': 0.05,         # Very slow/impaired learning rate due to Beta-Amyloid
            'ltd_rate': 0.4           # LTD might be slightly facilitated or normal
        }
    }
    return common, conditions

# ==============================================================================
# 3. RUN SIMULATION
# ==============================================================================
def run_simulation(common, cond_params):
    """
    Runs the simulation for a specific condition (Healthy or AD).
    """
    time_steps = np.arange(0, common['total_time'], common['dt'])
    synaptic_weight = np.zeros(len(time_steps))
    synaptic_weight[0] = cond_params['w_initial']

    for i in range(len(time_steps) - 1):
        t = time_steps[i]
        w = synaptic_weight[i]
        
        # High-Frequency Stimulation (LTP Induction)
        if common['hfs_start'] <= t < common['hfs_end']:
            dw = cond_params['ltp_rate'] * (cond_params['w_max'] - w) * common['dt']
            synaptic_weight[i+1] = w + dw
            
        # Low-Frequency Stimulation (LTD Induction)
        elif common['lfs_start'] <= t < common['lfs_end']:
            dw = cond_params['ltd_rate'] * (cond_params['w_min'] - w) * common['dt']
            synaptic_weight[i+1] = w + dw
            
        # No Stimulation (Maintenance)
        else:
            synaptic_weight[i+1] = w

    return time_steps, synaptic_weight

# ==============================================================================
# 4. PLOT RESULTS
# ==============================================================================
def plot_results(common, results):
    plt.figure(figsize=(12, 7))
    
    # Plot Healthy Line
    plt.plot(results['Healthy']['time'], results['Healthy']['weight'], 
             label='Healthy Control', color='royalblue', linewidth=3)
    
    # Plot Alzheimer's Line
    plt.plot(results['Alzheimers']['time'], results['Alzheimers']['weight'], 
             label="Alzheimer's Disease (Aβ Pathology)", color='firebrick', linewidth=3, linestyle='--')

    # Formatting
    plt.title('Impact of Alzheimer’s Pathology on Schaffer Collateral Plasticity', fontsize=16)
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Synaptic Weight (Arbitrary Units)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Shaded Regions for Stimulation
    plt.axvspan(common['hfs_start'], common['hfs_end'], color='green', alpha=0.15, 
                label='High-Frequency Stimulation (LTP)')
    plt.axvspan(common['lfs_start'], common['lfs_end'], color='red', alpha=0.15, 
                label='Low-Frequency Stimulation (LTD)')

    plt.legend(loc='upper right', fontsize=10)
    plt.ylim(0, 3.0)
    plt.tight_layout()
    plt.show()

# ==============================================================================
# 5. MAIN EXECUTION
# ==============================================================================
if __name__ == '__main__':
    common_params, condition_params = setup_parameters()
    results = {}
    
    # Run for Healthy
    t, w = run_simulation(common_params, condition_params['Healthy'])
    results['Healthy'] = {'time': t, 'weight': w}
    
    # Run for Alzheimer's
    t, w = run_simulation(common_params, condition_params['Alzheimers'])
    results['Alzheimers'] = {'time': t, 'weight': w}
    
    # Plot Comparison
    plot_results(common_params, results)