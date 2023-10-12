//Переключение вкладок
function openPage(pageName, elmnt) {
  // Скрыть все элементы class="tabcontent" по умолчанию */
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Удалите цвет фона всех ссылок/кнопок вкладок
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
    tablinks[i].style.color = "";
  }

  // Показать содержимое конкретной вкладки
  document.getElementById(pageName).style.display = "block";

  // Добавить конкретный цвет кнопки, используемой для открытия содержимого вкладки
  elmnt.style.backgroundColor = '#242424';
  elmnt.style.color = '#FDF9F6';
}
// Получите элемент с id="defaultOpen" и нажмите на него
document.getElementById("defaultOpen").click();


// ------------------------------------------

//Фильтр в вендорах
function myFunction() {
  // Объявлять переменные
  var input, filter, ul, li, a, i;
  input = document.getElementById("mySearch");
  filter = input.value.toUpperCase();
  ul = document.getElementById("myMenu");
  li = ul.getElementsByTagName("li");


  // Выполните цикл по всем элементам списка и скройте те, которые не соответствуют запросу поиска
  for (i = 0; i < li.length; i++) {
    a = li[i].getElementsByTagName("a")[0];
    if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}

// -------------------------------------
//Переключение вопросов
function openQuest(pageName, elmnt) {
  // Скрыть все элементы class="tabcontent" по умолчанию */
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("dropdown-container");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  // Удалите цвет фона всех ссылок/кнопок вкладок
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }

  // Показать содержимое конкретной вкладки
  document.getElementById(pageName).style.display = "block";

  // Добавить конкретный цвет кнопки, используемой для открытия содержимого вкладки
  elmnt.style.backgroundColor = 'lightgray';
}

// ----------------------------------------------------------
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    /* Переключение между добавлением и удалением класса "active",
    чтобы выделить кнопку, управляющую панелью */
    this.classList.toggle("active");

    /* Переключение между скрытием и отображением активной панели */
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}


function showAnswer(name) {
  var contFAQ = document.getElementsByClassName("contentFAQ");
  for (var i = 0; i < contFAQ.length; i++) {
    contFAQ[i].style.display = "none";
  }
  var answerFAQ = document.getElementById(name);
  if (answerFAQ.style.display === "block") {
    answerFAQ.style.display = "none";
  } else {
    answerFAQ.style.display = "block";
  }

  console.log(name);
}
