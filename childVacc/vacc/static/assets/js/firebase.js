// you should set your firebaseConfig file
// visit https://console.firebase.google.com/u/1/project/projectID/settings/general/
// var firebaseConfig = {
//     apiKey: "######YOUR API KEY#####",
//     authDomain: "projectId.firebaseapp.com",
//     databaseURL: "https://projectId.firebaseio.com",
//     projectId: "projectId",
//     storageBucket: "projectId.appspot.com",
//     messagingSenderId: "######messagingSenderId######",
//     appId: "######## appI d#########",
//     measurementId: "#### measurementId ####"
// };

const firebaseConfig = {
    apiKey: "AIzaSyAbCSVC8yDxih3j7aIf__dFKQ64YlCwz3A",
    authDomain: "childvacc-614df.firebaseapp.com",
    databaseURl: "https://childvacc-614df-default-rtdb.firebaseio.com/",
    projectId: "childvacc-614df",
    storageBucket: "childvacc-614df.appspot.com",
    messagingSenderId: "632778258197",
    appId: "1:632778258197:web:28b9296e8a236916ff1b1c",
    measurementId: "G-B9K63X6VB3"
  };
firebase.initializeApp(firebaseConfig);
var db = firebase.firestore();
db.collection('notifications').where("is_read", "==", false).onSnapshot(function
    (querySnapshot) {
    var undreaded_box = document.getElementById('undreaded_box');
    undreaded_box.innerHTML = '';
    querySnapshot.forEach(function (snapshot) {
        undreaded_box.innerHTML +=
            `<div id="` + snapshot.id + `" class="alert alert-success" role="alert">
                    <h4 class="alert-heading">New Message</h4>
                    <p>` + snapshot.data().message + `</p>
                    <hr>
                    <a href="#" class="make_as_read_link">Make As Read</a>
                 </div>`;
        $('.make_as_read_link').click(function (e) {
            e.preventDefault();
            makeAsRead(snapshot.id);
        });
    });
});
db.collection('notifications').where("is_read", "==", true).onSnapshot(function
    (querySnapshot) {
    var readed_box = document.getElementById('readed_box');
    readed_box.innerHTML = '';
    querySnapshot.forEach(function (snapshot) {
        readed_box.innerHTML +=
            `<div id="` + snapshot.id + `" class="alert alert-primary" role="alert">
                    <h4 class="alert-heading">Old Message</h4>
                    <p>` + snapshot.data().message + `</p>
                 </div>`;
    });
});

function makeAsRead(snapshot_id) {
    $.ajax("/ajax/make-as-read/?snapshot_id=" + snapshot_id, {
        success: function (data) {
            console.log(data);
        }
    });
}

function sendMessage() {
    var message_element = document.getElementById('id_message');
    $.ajax('/ajax/send-message?message=' + message_element.value, {
        success: function (data) {
            console.log(data);
            message_element.value = '';
        }
    });
}