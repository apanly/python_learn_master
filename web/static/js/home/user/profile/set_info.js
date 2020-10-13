;
var profile_set_info_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var that = this;
        $("#pop_layer .profile_set_info_wrap .save").click(function() {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在保存，请不要重复提交~~");
                return false;
            }

            var name_target = $('#pop_layer .profile_set_info_wrap input[name=name]');
            var name = name_target.val();

            var email_target = $('#pop_layer .profile_set_info_wrap input[name=email]');
            var email = email_target.val();


            if ( !common_ops.validate.length(name,2 ) ) {
                common_ops.tip("请输入符合规范的姓名，至少2个字符~~", name_target);
                return;
            }

            if ( !common_ops.validate.email(email  ) ) {
                common_ops.tip("请输入符合规范的邮箱~~", email_target);
                return;
            }

            var data = $("#pop_layer .profile_set_info_wrap form").serialize();

            btn_target.addClass("disabled");
            $.ajax({
                url: home_common_ops.buildUrl("/profile/set_info"),
                data: data,
                type: 'POST',
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if (res.code == 200) {
                        callback = function(){
                            window.location.href=window.location.href;
                        };
                    }
                    common_ops.msg(res.msg,res.code == 200, callback);
                }
            });

        });
    }
};
$(document).ready(function () {
    profile_set_info_ops.init();
});