import logging
import pandas as pd

# Configure logging
logging.basicConfig(filename='computation_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Log computations
logging.info('Computation 1: ...')
logging.info('Computation 2: ...')

# Save logs as TSV
with open('computation_log.tsv', 'w') as tsv_file:
    for line in open('computation_log.txt'):
        tsv_file.write(line.replace(' - ', '\t'))

# Save logs as CSV
df = pd.read_csv('computation_log.tsv', delimiter='\t')
df.to_csv('computation_log.csv', index=False)
