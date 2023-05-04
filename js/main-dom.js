$(document).ready(function () {
  configurarInputsCategoria();
});

/**
 * Configura a lógicas dos inputs para categorias.
 */
function configurarInputsCategoria() {
  const $inputsCategorias = $("input[name=categoria]");
  $inputsCategorias.change(function () {
    $inputsCategorias.each(function () {
      if (this.checked) {
        toogleCard(this, true);
      } else {
        toogleCard(this, false);
      }
    });
  });
}

/**
 * Realiza o toggle para os cards.
 * @param {*} labelWrapper
 * @param {*} bMarcar
 */
function toogleCard(labelWrapper, bMarcar) {
  const $label = $(labelWrapper).parent();
  const $divCard = $(labelWrapper).next();
  if (bMarcar) {
    $label.addClass("label-selecionado");
    $divCard.addClass("card-selecionado");
  } else {
    $label.removeClass("label-selecionado");
    $divCard.removeClass("card-selecionado");
  }
}
