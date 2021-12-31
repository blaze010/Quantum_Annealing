Note: This repo draws heavily from https://github.com/xBorox1/D-Wave-VRP. I have made some modifications to the original code which are basically some library updations and some feature enhancements, these are described below.

# Qunatum Annealing based solution for MDVRP
The solution presented in the original repo has been modified in the following aspects:
* qbsolv() has been replaced by LeapHybridBQMSampler() as support for qbsolv() has been depreciated
* The code has been modified to show the time taken for running the optimization along with the results
* A few new test cases have been added
