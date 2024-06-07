console.log("working ok on ubuntu:)\n\n");
const path = require('path');
const { app, BrowserWindow } = require('electron')

const createWindow = () => {
    const win = new BrowserWindow({
    minWidth:400,
    minHeight: 550,
    maxWidth:400,
    maxHeight: 550,
    webPreferences:{
        preload: path.join(__dirname, 'preload.js')
    }
    })
    
    win.loadURL('http://127.0.0.1:5000');
}


app.whenReady().then(()=> {
    createWindow()
})