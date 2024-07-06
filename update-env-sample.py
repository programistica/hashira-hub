import os

def load_env_file(file_path):
    """ Load environment variables from a file. """
    env_vars = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    env_vars[key] = value
    return env_vars

def update_env_sample(env_path, sample_path):
    env_vars = load_env_file(env_path)
    sample_vars = load_env_file(sample_path)

    with open(sample_path, 'w') as file:
        for key in env_vars.keys():
            if key in sample_vars:
                file.write(f'{key}={sample_vars[key]}\n')
            else:
                file.write(f'{key}=your_value_here\n')

if __name__ == '__main__':
    env_path = '.env'
    sample_path = '.env.sample'
    update_env_sample(env_path, sample_path)
