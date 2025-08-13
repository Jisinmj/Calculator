<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Calculator</title>
  <style>
    *{box-sizing:border-box;font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial}
    body{display:flex;min-height:100dvh;margin:0;align-items:center;justify-content:center;background:#0f172a}
    .app{width:min(360px,92vw);background:#111827;border-radius:20px;box-shadow:0 10px 30px rgba(0,0,0,.35);padding:18px}
    .screen{background:#0b1220;color:#e5e7eb;border-radius:14px;padding:16px;text-align:right;font-size:28px;min-height:64px;word-wrap:break-word}
    .keys{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:14px}
    button{border:0;border-radius:14px;padding:16px;font-size:18px;background:#1f2937;color:#f9fafb;cursor:pointer}
    button.op{background:#334155}
    button.eq{background:#2563eb}
    button.wide{grid-column:span 2}
    button:active{filter:brightness(1.1)}
  </style>
</head>
<body>
  <div class="app">
    <div id="screen" class="screen">0</div>
    <div class="keys">
      <button class="op" data-fn="clear">C</button>
      <button class="op" data-fn="back">⌫</button>
      <button class="op" data-op="%">%</button>
      <button class="op" data-op="/">÷</button>

      <button data-num="7">7</button>
      <button data-num="8">8</button>
      <button data-num="9">9</button>
      <button class="op" data-op="*">×</button>

      <button data-num="4">4</button>
      <button data-num="5">5</button>
      <button data-num="6">6</button>
      <button class="op" data-op="-">−</button>

      <button data-num="1">1</button>
      <button data-num="2">2</button>
      <button data-num="3">3</button>
      <button class="op" data-op="+">+</button>

      <button class="wide" data-num="0">0</button>
      <button data-num=".">.</button>
      <button class="eq" data-eq="=">=</button>
    </div>
  </div>

  <script>
    const screen = document.getElementById("screen");
    let a = "", b = "", op = null, justEq = false;

    const render = () => {
      let shown = b || a || "0";
      screen.textContent = shown;
    };

    const putNum = (n) => {
      if (justEq) { a=""; b=""; op=null; justEq=false; }
      if (!op) {
        if (n === "." && a.includes(".")) return;
        if (n === "0" && a === "0") return;
        a = (a === "0" && n !== ".") ? n : (a + n);
      } else {
        if (n === "." && b.includes(".")) return;
        if (n === "0" && b === "0") return;
        b = (b === "0" && n !== ".") ? n : (b + n);
      }
      render();
    };

    const setOp = (o) => {
      if (a === "" && screen.textContent !== "0") a = screen.textContent;
      if (a !== "" && b !== "") { equals(); a = screen.textContent; b=""; }
      op = o; justEq = false; render();
    };

    const clearAll = () => { a=""; b=""; op=null; justEq=false; render(); };
    const back = () => {
      if (justEq) return;
      if (op) { b = b.slice(0,-1); }
      else { a = a.slice(0,-1); }
      render();
    };

    const equals = () => {
      if (a === "" || !op || b === "") return;
      const x = parseFloat(a), y = parseFloat(b);
      let res = 0;
      switch(op){
        case "+": res = x + y; break;
        case "-": res = x - y; break;
        case "*": res = x * y; break;
        case "/": res = y === 0 ? "Error" : x / y; break;
        case "%": res = x % y; break;
      }
      screen.textContent = String(res);
      a = String(res); b = ""; op = null; justEq = true;
    };

    document.addEventListener("click", (e)=>{
      const t=e.target;
      if (t.dataset.num) putNum(t.dataset.num);
      if (t.dataset.op)  setOp(t.dataset.op);
      if (t.dataset.eq)  equals();
      if (t.dataset.fn==="clear") clearAll();
      if (t.dataset.fn==="back")  back();
    });

    // Keyboard support
    document.addEventListener("keydown", (e)=>{
      if ("0123456789.".includes(e.key)) putNum(e.key);
      if ("+-*/%".includes(e.key)) setOp(e.key);
      if (e.key==="Enter" || e.key==="=") equals();
      if (e.key==="Backspace") back();
      if (e.key==="Escape") clearAll();
    });

    render();
  </script>
</body>
</html>
