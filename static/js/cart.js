var updateBtns = document.getElementsByClassName("update-cart");
for (var i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log("productId: ", productId, "action: ", action)
    // var user=Request.user
    console.log("user:", user)
    if (user === "AnonymousUser") {
      console.log("not logged in")
    } else {
      updateUserCartOrder(productId, action)
    }
  })
}

function updateUserCartOrder(productId, action) {
  console.log(productId, "user logging in,sending data")
  var url = '/update_item/'
  fetch(url, {
    method: "POST",
    headers: {
      "content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ 'productID': productId, 'action': action })
  })
    .then((response) => { return response.json() })
    .then((data) => {
      console.log('data', data)
      location.reload()
    })
}
