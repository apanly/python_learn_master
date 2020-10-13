;
var grant_assign_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $("#grant-action .save").click(function () {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在保存，请不要重复提交~~");
                return false;
            }
            var data = $("#grant-action").serialize();
            btn_target.addClass("disabled");
            $.ajax({
                url: home_common_ops.buildUrl('/rbac/grant/assign'),
                data: data,
                type: 'POST',
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = {};
                    if (res.code == 200) {
                        callback = function () {
                            window.location.href = window.location.href;
                        }
                    }
                    common_ops.msg(res.msg, res.code == 200, callback);
                }
            });
        });
    }
};

$(document).ready(function () {
    grant_assign_ops.init();
});