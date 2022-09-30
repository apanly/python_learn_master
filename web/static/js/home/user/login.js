;
var user_login_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $(".login_wrap_email .do_login").click(function () {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }

            var email_target = $(".login_wrap input[name=email]");
            var email = email_target.val();
            var pwd_target = $(".login_wrap input[name=pwd]");
            var pwd = pwd_target.val();

             if ( !common_ops.validate.email( email ) ) {
                common_ops.tip("请输入符合规范的邮箱~~",email_target);
                return;
            }
             if (!common_ops.validate.length(pwd)) {
                common_ops.tip("请输入符合规范邮箱授权码~~",pwd_target);
                return;
            }
            btn_target.addClass("disabled");
            $.ajax({
                url: home_common_ops.buildUrl("/user/login"),
                type: 'POST',
                data: {'email': email, 'pwd': pwd},
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code == 200) {
                        callback = function () {
                            window.location.href = res.data.next_url;
                        }
                    }
                    common_ops.msg(res.msg,res.code == 200, callback);
                }
            })
        });

        //切换微信登录
        $(".switch_wechat").click(function () {
            $(".login_wrap_email").hide();
            $(".login_wrap_wechat").show();
            //微信登录
            var obj = new WxLogin({
                id: "login_wrap_wechat",
                appid: $(".hidden_val_wrap input[name=wechat_open_appid]").val(),
                scope: "snsapi_login",
                redirect_uri: home_common_ops.buildUrl("/oauth/open-login"),
                state: "",
                style: "",
                href: ""
            });
        });

        $(".switch_email").click(function () {
            $(".login_wrap_email").show();
            $(".login_wrap_wechat").hide();
        });

        var can_switch_wechat = $(".hidden_val_wrap input[name=wechat_open_appid]").val();
        can_switch_wechat = ( can_switch_wechat != undefined && can_switch_wechat.length > 1);
        if( can_switch_wechat ){
            $(".switch_wechat").click();
        }else{
            $(".switch_email").click();
        }
    }

};

$(document).ready(function () {
    user_login_ops.init();
});