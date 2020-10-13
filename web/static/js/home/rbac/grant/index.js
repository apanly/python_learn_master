;
var grant_index_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var that = this;
        $(".add_action,.edit_action").click( function(){
            var url = home_common_ops.buildUrl("/rbac/grant/set");
            common_ops.popLayer(url ,$(this).data());
        } );


        $(".grant_list_wrap .ops").click(function () {
            var btn_target = $("this");
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在保存，请不要重复提交~~");
                return false;
            }
            var data = {
                'id': $(this).data('id'),
                'act': $(this).data('act')
            };
            var callback = {
                "ok": function () {
                    $.ajax({
                        url: home_common_ops.buildUrl('/rbac/grant/ops'),
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
                },
                "cancel": function () {

                }
            };
            common_ops.confirm("确认设置为 " + $(this).text() + " ?", callback);
        });
    }
};

$(document).ready(function () {
    grant_index_ops.init();
});