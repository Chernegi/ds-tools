# Visualisation os network and graphs
https://towardsdatascience.com/visualizing-networks-in-python-d70f4cbeb259
https://www.geeksforgeeks.org/visualize-graphs-in-python/


# Setup dependencies
brew install ffmpeg
pip install poetry

poetry install



# Run jupyter notebook:
poetry run jupyter lab --NotebookApp.ResourceUseDisplay.track_cpu_percent=True --NotebookApp.ResourceUseDisplay.mem_limit=6442450944 --ServerApp.iopub_data_rate_limit=1000000000 --ServerApp.rate_limit_window=120
