# Merge Conflict Resolution

## Overview
A merge conflict was intentionally created while integrating the feature branches into the `main` branch as part of the collaboration workflow.

## Conflicted Files
1. app/main.py  
2. app/services/image_service.py  
3. __pycache__/ (generated Python bytecode files)

## Cause of Conflict

### main.py
Both `feature/translation` and `feature/image-generation` branches modified `main.py`.  
The translation branch removed the image router, while the image-generation branch added it.  
This caused Git to report a complex conflict that could not be resolved using the GitHub UI.

### image_service.py
The file existed only in the `feature/image-generation` branch and had been removed from the `feature/translation` branch, leading to a conflict during merge.

### __pycache__ Files
The `__pycache__` directory was accidentally committed in multiple branches, causing conflicts because the generated `.pyc` files differed between environments.

## Resolution Steps
- The pull request that caused the complex conflict was closed.
- All `__pycache__` directories and `.pyc` files were removed from the repository in both branches, as they are generated artifacts and should not be version-controlled.
- The correct and latest implementation of `image_service.py` from the image-generation feature was kept in the `main` branch.
- `main.py` was manually edited to include both routers:

```python
app.include_router(translation.router)
app.include_router(image_gen.router)

