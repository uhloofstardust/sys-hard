const { app, BrowserWindow } = require("electron");

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
  });

  win.loadFile("public/index.html");
}

app.whenReady().then(createWindow);
app.on("before-quit", () => {
  // we need to close the flask server here, i'm unable to figure it out
});
