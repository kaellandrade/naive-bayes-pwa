async function main() {
  let pyodide = await loadPyodide();
  await pyodide.loadPackage("pandas")
  return pyodide;
  
}

let pyodideSobscribePromisse = main();

async function evaluatePython() {
  let pyodide = await pyodideSobscribePromisse;
  try {
    let python_code = await (await fetch("/python/main.py")).text();
    pyodide.runPython(python_code, pyodide);
  } catch (err) {
    console.log(err);
  }
}
evaluatePython();
