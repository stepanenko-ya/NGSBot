function buttonSendMessage() {

    let message = document.getElementById('new_message_field').value;
    let userId = document.getElementById('current_message_container').getAttribute('data-user_id');

    // Create new line for message
    let newBlock = document.createElement("div");
    newBlock.classList.add("message_row");
    newBlock.innerHTML = "<strong>Вы:</strong><br>" +  message;

    let messageCont = document.getElementById("current_message_container");
    messageCont.appendChild(newBlock);
    // End - Create new line for message

    $.ajax({
        url: "ajax_send_message/",
        typte: 'POST',
        data: {"message_text": message,
               "user_id": userId},
        cache: true,
        success: function (data) {
            console.log("AJAX - Ok");
        },
        error: function () {
            console.log("AJAX - ERROR");
        }
    });
};


setInterval(function () {

    let userId = document.getElementById('current_message_container').getAttribute('data-user_id');

    $.ajax({
        url: "update_ajax/",
        typte: 'GET',
        data: {"user_id": userId},
        cache: true,
        success: function (data) {

            if (data["message"] != ""){

                // Create new line for message
                let newBlock = document.createElement("div");
                newBlock.innerHTML = "<strong>Админ:</strong><br>" +  data["message"];
                newBlock.classList.add("message_row");

                let messageCont = document.getElementById("current_message_container");
                messageCont.appendChild(newBlock);
                // End - Create new line for message

            }
        },
        error: function () {
            console.log("AJAX - ERROR");
        }
    });
}, 1000);




