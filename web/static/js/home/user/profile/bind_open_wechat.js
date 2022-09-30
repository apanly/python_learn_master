;
var bind_open_wechat_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var obj = new WxLogin({
            id: "login_wrap_wechat",
            appid: $(".hidden_val_wrap input[name=wechat_open_appid]").val(),
            scope: "snsapi_login",
            redirect_uri: home_common_ops.buildUrl("/oauth/open-bind"),
            state: "",
            style: "",
            href: ""
        });
    }
};

$(document).ready(function () {
    bind_open_wechat_ops.init();
});