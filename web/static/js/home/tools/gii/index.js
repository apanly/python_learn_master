;
var gii_index_ops = {
    init: function () {
        this.eventBind();
        this.resetBoxHeight();
    },
    eventBind: function () {
    },
    resetBoxHeight: function () {
        var body_height = 0;
        $(".box .box-body").each(function () {
            if ($(this).height() >= body_height) {
                body_height = $(this).height();
            }
        });

        var title_height = 0;
        $(".box .box-header").each(function () {
            if ($(this).height() >= title_height) {
                title_height = $(this).height();
            }
        });
        $(".box .box-body").height(body_height);
        $(".box .box-header").height(title_height);
    }
};

$(document).ready(function () {
    gii_index_ops.init();
});