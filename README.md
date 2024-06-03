![COMFY-UI](https://github.com/daxcay/ComfyUI-NODEJS/assets/164315771/1b5fcdbf-ec3e-4a43-8311-43e20d73b705)

# ComfyUI-NODEJS

This node allows the execution of Node.js application within ComfyUI by leveraging the **ComfyUI-NODEJS**, which starts alongside ComfyUI and facilitates the installation of Node.js. The integration enables Python subprocesses to execute Node.js scripts.

## Features:

- Node.js Installer: An semi-automated installation process of nodejs for windows users only.
- Package Installer: Supports the installation and automatic updating of Node.js packages upon each startup.
- Multiple scripts Execution: Enables running multiple projects simultaneously.
- Graceful Shutdown: The service terminates when ComfyUI exits.

## NodeJS Installation:

**Note: For non-windows user please install NodeJS before running this node**

**NodeJS Installation: https://nodejs.org/en/download**

**Windows users can skip this section**

For any query you can join my discord server: https://discord.gg/Z44Zjpurjp

## Node Installation:

1. Using **comfy-cli**

   ```comfy node registry-install comfyui-nodejs```
   
3. Using **manual method**
   - Go to your Comfyui > Custom Nodes folder
   - Run CMD from folder path box or right click on empty area and click open in terminal.
   - Copy and Paste this command git clone ```https://github.com/daxcay/ComfyUI-NODEJS.git```
   - Then go inside ComfyUI-NODEJS with cmd or open new and type pip install -r requirements.txt to install the requirements.

4. Using Comfy Manager (https://github.com/ltdrdata/ComfyUI-Manager)
   - Inside ComfyUI > Click Manager Button on Side.
   - Click Install Custom Node and Search for nodejs and Install this node:
     
   ![image](https://github.com/daxcay/ComfyUI-NODEJS/assets/164315771/8cb85775-0eb0-4392-b4c3-979785a86a13)

   - Restart ComfyUI and it should be good to go

## Configuration

To run nodejs project(s) you will need to do paste your project(s) folder in the **nodejs** directory of **ComfyUI-NODEJS**. 

```ComfyUI\custom_nodes\ComfyUI-NODEJS\nodejs```

![image](https://github.com/daxcay/ComfyUI-NODEJS/assets/164315771/9adabe4a-c25a-4604-85f3-7f2020167f30)

![image](https://github.com/daxcay/ComfyUI-NODEJS/assets/164315771/c6d990c0-7f3e-40ef-8a20-874d798f2c7b)

**To run a project successfully verify the below steps carefully.**

### Project structure to be followed

Every project should have two mandatory files in root folder one **app.js** and another **package.json** like this 

![image](https://github.com/daxcay/ComfyUI-NODEJS/assets/164315771/c6731bf1-6db8-479f-ba53-f593a1bcf31f)

**app.js** is just for representation actual name could be anything. (main.js, foo.js). 
but in package.json file mention correct name.

**package.json** looks something like this:

```
{
  "name": "project1",
  "version": "1.0.0",
  "description": "",
  "main": "app.js",
  "scripts": {
    "dev" : "node dev.js",
    "production" : "node app.js",
    "test": "node test.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.19.2"
  }
}
```

Ensure your project package.json to have a "production" script in scripts objects.

![image](https://github.com/daxcay/ComfyUI-NODEJS/assets/164315771/af32aef5-87e6-41f2-b095-6ee8798b0977)

Now run/restart **comfyui**. 

Open any browser and head to ```http://localhost:3000```. If NodeJs is installed successfully it should return:

![image](https://github.com/daxcay/ComfyUI-NODEJS/assets/164315771/480baf8e-6a37-44fe-8e7d-c012dc637fcd)

**Demo projects are given in nodejs folder in case you don't understand anything. delete them when running actual projects or build upon them.**


# CREDITS

◉ Daxton Caylor - ComfyUI Node Developer 
- Discord - daxtoncaylor
- Email - daxtoncaylor@gmail.com
- Discord server: https://discord.gg/Z44Zjpurjp
- Commission Status:  🟢 **Open** 🟢

# Support ❤️
- Buy me a coffee: https://buymeacoffee.com/daxtoncaylor
- If you like to suppport me you can donate me on paypal: https://paypal.me/daxtoncaylor
 









