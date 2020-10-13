;
var staff_set_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var that = this;
        $(".staff_set_wrap .save").click(function () {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在保存，请不要重复提交~~");
                return false;
            }

            var name_target = $(".staff_set_wrap input[name=name]");
            var name = name_target.val();

            var email_target = $(".staff_set_wrap input[name=email]");
            var email = email_target.val();

            var role_id_target = $(".staff_set_wrap select[name=role_id]");
            var role_id = role_id_target.val();


            if( !common_ops.validate.length( name,1,10 )) {
                common_ops.tip("请输入符合规范的姓名~~", name_target);
                return;
            }
            if( !common_ops.validate.email( email )) {
                common_ops.tip("请输入符合规范的邮箱~~", email_target );
                return;
            }

            if( role_id < 1 ){
                common_ops.tip("请选择部门（顶级部门不可选择）~~", role_id_target );
                return;
            }

            var data = $(".staff_set_wrap form").serialize();
            btn_target.addClass("disabled");

            $.ajax({
                url: home_common_ops.buildUrl('/rbac/staff/set'),
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
    staff_set_ops.init();
});
