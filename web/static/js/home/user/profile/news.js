;
var news_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $(".news_wrap .ops").click(function(){
            var btn_target = $("this");
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在保存，请不要重复提交~~");
                return false;
            }
            var data = {
                'id': $(this).data('id')
            };
            var callback = {
                "ok": function () {
                    $.ajax({
                       url: home_common_ops.buildUrl("/profile/news/ops"),
                        type: "POST",
                        data: data,
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

        $(".batch_ops").click(function(){
            var btn_target = $("this");
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在保存，请不要重复提交~~");
                return false;
            }
            var callback = {
                "ok": function () {
                    $.ajax({
                       url: home_common_ops.buildUrl("/profile/news/batch_ops"),
                        type: "POST",
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
            common_ops.confirm("将所有未读信息标记为已读 ?", callback);
        });
    }
};

$(document).ready(function () {
    news_ops.init();
});