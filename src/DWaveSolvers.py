# File simplifies communication with DWave solvers. 

from dwave_qbsolv import QBSolv
from dwave.system import DWaveSampler, EmbeddingComposite, LeapHybridBQMSampler
import hybrid

# Creates hybrid solver with hardcoded configuration.
def hybrid_solver():
    workflow = hybrid.Loop(
        hybrid.RacingBranches(
        hybrid.InterruptableTabuSampler(),
        hybrid.EnergyImpactDecomposer(size=30, rolling=True, rolling_history=0.75)
        | hybrid.QPUSubproblemAutoEmbeddingSampler()
        | hybrid.SplatComposer()) | hybrid.ArgMin(), convergence=1)
    return hybrid.HybridSampler(workflow)

# Gets cpu or qpu solver.
# For qpu hybrid solver is used. For cpu qbsolv.
def get_solver(solver_type):
    solver = None
    if solver_type == 'cpu':
        #solver = hybrid_solver()
        solver = LeapHybridBQMSampler()
    if solver_type == 'qpu':
        solver = EmbeddingComposite(DWaveSampler())
    return solver

# Solves qubo on qpu. Returns list of solutions.
def solve_qubo(qubo, solver_type = 'cpu'):
    sampler = get_solver(solver_type)
    response = sampler.sample_qubo(qubo.dict)
    if(solver_type == 'qpu'):
    	print(response.info["timing"])
    	print(response.samples)
    else:
    	print(response.info)
    	print(response.samples)
    return list(response)[0]
    
