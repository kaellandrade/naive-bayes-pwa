async function main() {
  let pyodide = await loadPyodide();
  await pyodide.loadPackage("pandas");
  await pyodide.loadPackage("ssl");
  return pyodide;
}

let pyodideSobscribePromisse = main();

async function evaluatePython() {
  let loader = document.getElementById("loader");
  let formHome = document.getElementById("fomulario-home");

  loader.style.display = "block";
  formHome.style.filter = "blur(.2rem)";

  let pyodide = await pyodideSobscribePromisse;
  try {
    let python_code = await (await fetch("/python/main.py")).text();
    pyodide.runPython(python_code, pyodide);
    console.log("Fim");
  } catch (err) {
    console.log(err);
  } finally {
    loader.style.display = "none";
    formHome.style.filter = "blur(0)";
  }
}
evaluatePython();
