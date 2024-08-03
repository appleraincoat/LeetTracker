document.addEventListener('DOMContentLoaded', function() {
    var textareas = document.getElementsByTagName('textarea');
    for (var i = 0; i < textareas.length; i++) {
        textareas[i].addEventListener('keydown', function(e) {
            if (e.key == 'Tab' && !e.shiftKey) {
                e.preventDefault();
                var start = this.selectionStart;
                var end = this.selectionEnd;

                // Set textarea value to: text before caret + 4 spaces + text after caret
                this.value = this.value.substring(0, start) +
                             "    " + this.value.substring(end);

                // Put caret at right position again
                this.selectionStart =
                this.selectionEnd = start + 4;
            }
        });
    }
});