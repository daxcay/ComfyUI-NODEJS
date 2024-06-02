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

import subprocess
import shutil

class NodeScriptRunner:
    def __init__(self, js_file):
        self.js_file = js_file
        self.process = None

    def check_for_node_js(self):
        return (shutil.which('node') is not None)

    def run_js(self, args):
        try:
            if self.check_for_node_js() is not True:
                return
            final_args = ["node", self.js_file]
            final_args.extend(args)            
            self.process = subprocess.Popen(final_args)
            print(f"JavaScript file '{self.js_file}' is running in the background.")
        except FileNotFoundError:
            print("Node.js is not installed or not found in the system path.")
        except: 
            print('NodeJS failed to start script.')

    def terminate_background_js(self):
        if self.process:
            self.process.terminate()
            print(f"Terminated the background JavaScript process.")
        else:
            print("No background JavaScript process is running.")

    def __del__(self):
        self.terminate_background_js()
