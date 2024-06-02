# Copyright 2024 Daxton Caylor
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
@author: Daxton Caylor
@title: ComfyUI-NODEJS
@nickname: ComfyUI-NODEJS
@description: This node enables someone to run any nodejs application alongside comfyui.
"""

import os
from .classes.NodeInstaller import NodeInstaller
from .classes.NodeScriptRunner import NodeScriptRunner
from .config import *

NODE_JS_SCRIPTS_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), NODE_JS_SCRIPTS_FOLDER)

if IS_ACTIVE:
    nodeInstaller = NodeInstaller(NODE_JS_INSTALLER_URL)
    if nodeInstaller.check_for_node_js() is not True:
        nodeInstaller.download_nodejs()
        nodeInstaller.install_nodejs()
    nodeInstaller.install_all_packages(NODE_JS_PACKAGES)

    for script in NODE_RUNNABLES:
        nodeScriptRunner = NodeScriptRunner(os.path.join(NODE_JS_SCRIPTS_FOLDER, script))
        nodeScriptRunner.run_js(NODE_RUNNABLES_ARGS[script])

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# WEB_DIRECTORY = "./web"
