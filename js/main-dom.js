$(document).ready(function () {
  configurarInputsCategoria("categoria");
  configurarInputsCategoria("idade");
  configurarInputsCategoria("porte");
});

/**
 * Configura a lógicas dos inputs para categorias.
 */
function configurarInputsCategoria(sCategoria) {
  const $inputsCategorias = $(`input[name=${sCategoria}]`);
  $inputsCategorias.change(function () {
    validarForm();
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
    $divCard.addClass("ripple");
  } else {
    $label.removeClass("label-selecionado");
    $divCard.removeClass("card-selecionado");
  }
}

/**
 * Valida o formulário.
 */
function validarForm() {
  const categoria = $("input:radio[name='categoria']:checked").val();
  const porte = $("input:radio[name='porte']:checked").val();
  const idade = $("input:radio[name='idade']:checked").val();

  if (categoria && porte && idade) {
    $("#btn-enviar").prop("disabled", false);
  }
}
