const url = 'http://127.0.0.1:5000/score';
const btnNewScore = document.getElementById("new-score");
const form = document.getElementById('client-form');
/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postScoreClassification = () => {


  const inputs = form.querySelectorAll('input');
  const formData = new FormData();
  inputs.forEach(input => {
    formData.append(input.name, input.value);
  });
  const msg_section = document.getElementById("msg-section");
  let msg = "Obtendo classificação...";
  msg_section.innerHTML = msg;

  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      if (data && data.score_classification) {
        msg = `<p class='msg-area'>Com base nos dados informados, o score de crédito classificado para esse cliente é <strong>${data.score_classification}</strong></p>`;
      } else {
        msg = `<p class='msg-area'>Ocorreu um erro ao tentar obter a classificação do score de crédito...</p>`;
      }
      msg_section.innerHTML = msg;

    })
    .catch((error) => {
      console.error('Error:', error);
      msg = `<p class='msg-area'>Ocorreu um erro na comunicação para tentar obter a classificação do score de crédito...</p>`;
      msg_section.innerHTML = msg;
    });
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  postScoreClassification();
});