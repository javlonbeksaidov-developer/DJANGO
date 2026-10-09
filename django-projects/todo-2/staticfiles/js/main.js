// Switch a row into edit mode and back
document.querySelectorAll("[data-start-edit]").forEach(function (btn) {
  btn.addEventListener("click", function () {
    var row = btn.closest(".item");
    row.classList.add("editing");
    var input = row.querySelector('.edit-form input[type="text"]');
    input.focus();
    input.setSelectionRange(input.value.length, input.value.length);
  });
});

document.querySelectorAll("[data-cancel-edit]").forEach(function (btn) {
  btn.addEventListener("click", function () {
    var row = btn.closest(".item");
    var input = row.querySelector('.edit-form input[type="text"]');
    input.value = input.defaultValue;
    row.classList.remove("editing");
  });
});

// Escape cancels editing
document.addEventListener("keydown", function (e) {
  if (e.key !== "Escape") return;
  var open = document.querySelector(".item.editing [data-cancel-edit]");
  if (open) open.click();
});

// Ask before destructive forms
document.querySelectorAll("form[data-confirm]").forEach(function (form) {
  form.addEventListener("submit", function (e) {
    if (!window.confirm(form.dataset.confirm)) e.preventDefault();
  });
});

// Block double submits
document.querySelectorAll("form").forEach(function (form) {
  form.addEventListener("submit", function (e) {
    if (e.defaultPrevented) return;
    form.querySelectorAll('button[type="submit"]').forEach(function (b) {
      setTimeout(function () {
        b.disabled = true;
      }, 0);
    });
  });
});
