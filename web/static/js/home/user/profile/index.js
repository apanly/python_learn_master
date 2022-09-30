;
var profile_index_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var that = this;
        $(".set_info").click( function(){
            common_ops.popLayer( home_common_ops.buildUrl("/profile/set_info") );
        } );

        $(".bind_wechat").click( function(){
            common_ops.popLayer( home_common_ops.buildUrl("/profile/bind_open_wechat") );
        });

        $(".unbind_wechat").click(function () {
            var callback = {
                "ok": function () {
                    $.ajax({
                        url: home_common_ops.buildUrl("/profile/unbind_open_wechat"),
                        type: "POST",
                        dataType: "json",
                        success: function (res) {
                            var callback = null;
                            if (res.code == 200) {
                                callback = function () {
                                    window.location.href = window.location.href;
                                };
                            }
                            common_ops.alert(res.msg, callback);
                        }
                    });
                }
            };
            common_ops.confirm("确认要解绑微信？", callback);
        });
    }
};
$(document).ready(function () {
    profile_index_ops.init();
});