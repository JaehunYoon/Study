var myModal = new Example.Modal({id= "modal"});

// modal-button에 event 걸기
$(".modal-button").click(function () {
    myModal.show();
});

// confirm_button에 event 걸기
$(".confirm_button").click(function () {
    alert("I am Modal Display~~");
    myModal.hide();
});