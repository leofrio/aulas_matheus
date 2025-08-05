
# Conda Environment and Package Management Cheat Sheet

## 📦 Environment Management

### 1. Create a new environment
```bash
conda create --name myenv python=3.10
```
Replace `myenv` with your environment name, and set the desired Python version.

### 2. List all environments
```bash
conda env list
```

### 3. Activate an environment
```bash
conda activate myenv
```

### 4. Deactivate the current environment
```bash
conda deactivate
```

### 5. Delete an environment
```bash
conda remove --name myenv --all
```

---

## 📦 Package Management

### 6. Install a package into the current environment
```bash
conda install numpy
```

To install into a specific environment without activating it:
```bash
conda install -n myenv numpy
```

### 7. Install from a specific channel
```bash
conda install -c conda-forge pandas
```

### 8. Remove a package
```bash
conda remove numpy
```

### 9. Update a package
```bash
conda update numpy
```

### 10. Update conda itself
```bash
conda update conda
```

---

## 🔍 Search and List Packages

### 11. Search for a package
```bash
conda search matplotlib
```

### 12. List all installed packages
```bash
conda list
```

---

## 📄 Export and Recreate Environments

### 13. Export the environment to a file
```bash
conda env export > environment.yml
```

### 14. Create environment from a `.yml` file
```bash
conda env create -f environment.yml
```