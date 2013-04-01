var Redactor = (function ($) {
    // Redactor palette attributes will accumulate here.
    var redactor_attrs = [];
    // Initialize all textareas with the ``redactor_content`` class
    // as a Redactor rich text area.
    $(function () {
        var redactor_fields = $("textarea.redactor_content");
        if (redactor_fields.length !== redactor_attrs.length) {
            window.alert("Number of registered attributes does not match the widget count.");
        }
        $("textarea.redactor_content").each(function (i) {
            var settings = redactor_attrs[i]
                $t = $(this);
            settings.imageUpload = '/redactor/do-photos-upload/',
            settings.imageGetJson = '/redactor/do-photos-recent/',
            settings.minHeight =200;
            settings.iframe = true;
            // Add a class to the field's label in the Django admin so it can
            // be styled as well.
            $t.parent("div").find("label").addClass("redactor_label");
            $t.redactor(settings);
        });
    });
    return {
        register: function () {
            var attrs = arguments.length !== 0 ? arguments[0] : null;
            redactor_attrs.push(attrs);
        }
    };
})(jQuery);
