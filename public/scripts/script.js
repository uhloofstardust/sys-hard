document.addEventListener("DOMContentLoaded", function () {
  const btn = document.querySelector("button");
  const output = document.querySelector("h1");

  btn.addEventListener("click", function (e) {
    e.preventDefault();
    fetch("http://127.0.0.1:2312/hello", { method: "GET" })
      .then((res) => res.text())
      .then((res) => {
        console.log(res);
        output.textContent = res;
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
});
