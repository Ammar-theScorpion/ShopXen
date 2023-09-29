$(document).ready(function () {
    var ajax = null;
    var csrftoken = $('[name="csrfmiddlewaretoken"]').val();
    console.log(csrftoken);

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            }
        }
    });
    $('#delete').click(function (event) {
        event.preventDefault()
        //tname = 'reverseString';
        if (ajax !== null) {
            return;
        }
        ajax = $.ajax({
            url: 'http://127.0.0.1:8000/delchat',
            method: 'POST',
            contentType: 'text/plain', // to prevent Django from treating the ajax as a form form the Query
            error: function (e) {
                console.log(e)
            },
            success: function (response) {
                $('#chat').text('')
            },
            complete: function () {
                ajax = null;
            }

        });
    });
    $('#query').click(function (event) {
        event.preventDefault()

        text = document.getElementById('message').value;
        if (ajax !== null) {
            return;
        }
        ajax = $.ajax({
            url: 'http://127.0.0.1:8000/chat',
            method: 'POST',
            contentType: 'text/plain', // to prevent Django from treating the ajax as a form form the Query
            data: {
                'query': text,
            },
            error: function (e) {
                console.log(e) // error handling 
            },
            success: function (response) {
                try {

                    // Display "Thinking..." message while waiting for the response
                    const incomingChatLi = createChatLi("Thinking...", "assistant-message");
                    chatbox.appendChild(incomingChatLi);
                    chatbox.scrollTo(0, chatbox.scrollHeight);

                    // Simulate a delay before showing the static response (e.g., 1 seconds)
                    setTimeout(() => {
                        generateResponse(incomingChatLi, response);
                    }, 1000); // Adjust the delay duration (in milliseconds) as needed



                    // var entries = response.split("@");
                    // console.log(entries)
                    // // only the bot reponse ?
                    // // this is a for loop that will split the repsonses into user messages and bot answers
                    // for (var i = 0; i < entries.length - 1; i += 3) {

                    //     var user = entries[i];
                    //     var bot = entries[i + 1]
                    //     let h3 = $("<h3>").text('user: ' + user);

                    //     $("#chat").append(h3);
                    //     h3 = $("<h3>").text('bot: ' + bot);
                    //     $("#chat").append(h3);
                    //     console.log("User: " + user);
                    //     console.log("Bot: " + bot);
                    // }
                } catch (e) { }
            },
            complete: function () {
                ajax = null;
            }

        });
    });


    // const sidebar = document.querySelector("#sidebar");
    // const hide_sidebar = document.querySelector(".hide-sidebar");
    // const new_chat_button = document.querySelector(".new-chat");
    // const user_menu = document.querySelector(".user-menu ul");
    // const show_user_menu = document.querySelector(".user-menu button");

    const chatbox = document.querySelector("body > main > ul");
    const chatInput = document.querySelector("#message");
    const sendChatBtn = document.querySelector(".send-button");

    // the height the the input box in the chatbot can handle before start scrolling
    const inputInitHeight = chatInput.scrollHeight;

    const createChatLi = (message, className) => {
        // Create a chat <li> element with passed message and className
        const chatLi = document.createElement("li");

        chatLi.classList.add(`${className}`);
        // let chatContent = className === "assistant-message" ? `<p></p>` : `<span class="material-symbols-outlined">smart_toy</span><p></p>`;
        let chatContent = className === "assistant-message" ? `<p></p>` : `<p></p>`;
        chatLi.innerHTML = chatContent;
        chatLi.querySelector("p").textContent = message;
        return chatLi; // return chat <li> element
    }

    const generateResponse = (chatElement, response) => {
        const messageElement = chatElement.querySelector("p");

        // Replace this with your static response
        messageElement.textContent = response;
        chatbox.scrollTo(0, chatbox.scrollHeight);
    }

    const handleChat = () => {
        const userMessage = chatInput.value.trim(); // Get user-entered message and remove extra whitespace
        if (!userMessage) return;

        // Clear the input textarea and set its height to default
        chatInput.value = "";
        chatInput.style.height = `${inputInitHeight}px`;

        // Append the user's message to the chatbox
        chatbox.appendChild(createChatLi(userMessage, "user-message"));
        chatbox.scrollTo(0, chatbox.scrollHeight);
    }

    sendChatBtn.addEventListener("click", handleChat);

    // hide_sidebar.addEventListener("click", function () {
    //     sidebar.classList.toggle("hidden");
    // });

    // show_user_menu.addEventListener("click", function () {
    //     if (user_menu.classList.contains("show")) {
    //         user_menu.classList.toggle("show");
    //         setTimeout(function () {
    //             user_menu.classList.toggle("show-animate");
    //         }, 200);
    //     } else {
    //         user_menu.classList.toggle("show-animate");
    //         setTimeout(function () {
    //             user_menu.classList.toggle("show");
    //         }, 50);
    //     }
    // });

    // const models = document.querySelectorAll(".model-selector button");

    // for (const model of models) {
    //     model.addEventListener("click", function () {
    //         document.querySelector(".model-selector button.selected")?.classList.remove("selected");
    //         model.classList.add("selected");
    //     });
    // }

    // const message_box = document.querySelector("#message");

    // message_box.addEventListener("keyup", function () {
    //     message_box.style.height = "auto";
    //     let height = message_box.scrollHeight + 2;
    //     if (height > 200) {
    //         height = 200;
    //     }
    //     message_box.style.height = height + "px";
    // });

    // function show_view(view_selector) {
    //     document.querySelectorAll(".view").forEach(view => {
    //         view.style.display = "none";
    //     });

    //     document.querySelector(view_selector).style.display = "flex";
    // }

    // new_chat_button.addEventListener("click", function () {
    //     show_view(".new-chat-view");
    // });

    // document.querySelectorAll(".conversation-button").forEach(button => {
    //     button.addEventListener("click", function () {
    //         show_view(".conversation-view");
    //     })
    // });

});