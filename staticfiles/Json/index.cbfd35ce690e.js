$(document).ready(function () {
  fetch("/products")
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      // Construir el HTML

      let products = data.map(function (product) {
        return `
          <div id="container" class="FilterDiv ${product.category}      ">
            <img src="/static/Sources/Products/${product.picture}"/>
            <div id="middle">
              <h1>${product.name}</h1>
              <a href="./Public/single_product.html">
                <a href="/product/${product.id}">Comprar</a>
              </a>
              <a href="./Public/single_product.html"></a>
            </div>
          </div>
        `;
      });

      $("#Products_List").append(products);

      filterSelection("all");
    });
});
