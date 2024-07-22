#!/bin/bash
python -m venv myenv
source myenv/bin/activate
curl https://github.com/plotly/orca/releases/download/v1.3.1/orca-1.3.1.AppImage -L -o orca 
chmod +x orca
mv orca myenv/bin/
pip install -r requirements.txt