;
var gii_model_ops = {
    init: function () {
        this.eventBind();
        this.previewPath();
    },
    eventBind: function () {
        var that = this;
        $(".gii_model_wrap select[name=table]").select2({
            language: "zh-CN",
            width: '100%'
        });

        $(".gii_model_wrap select[name=table]").change(function () {
            that.previewPath();
        });

        $(".gii_model_wrap input[name=path]").bind("input",function(){
            that.previewPath();
        });

        $(".gii_model_wrap .save").click(function () {
            var btn_target = $(this);
            if (btn_target.hasClass("disabled")) {
                common_ops.alert("正在保存，请不要重复提交~~");
                return false;
            }

            var table_target = $(".gii_model_wrap select[name=table]");
            var table = table_target.val();

            var path_target = $(".gii_model_wrap input[name=path]");
            var path = path_target.val();


            if (!common_ops.validate.length(table, 1, 30)) {
                common_ops.tip("请输入或者选择表~~", table_target);
                return;
            }
            if (!common_ops.validate.length(path, 1)) {
                common_ops.tip("请输入符合规范的路径~~", path_target);
                return;
            }

            var data = $(".gii_model_wrap form").serialize();
            btn_target.addClass("disabled");

            $.ajax({
                url: home_common_ops.buildUrl('/tools/gii/model'),
                data: data,
                type: 'POST',
                dataType: 'json',
                success: function (res) {
                    btn_target.removeClass("disabled");
                    var callback = {};
                    if (res.code == 200) {
                        common_ops.msg(res.msg, res.code == 200, callback);
                    } else {
                        common_ops.alert(res.msg);
                    }

                }
            });
        });
    },
    previewPath: function () {
        var prefix_path = $(".gii_model_wrap .prefix_path").text();
        var path = $(".gii_model_wrap input[name=path]").val();
        var table = $(".gii_model_wrap select[name=table]").val();
        var model_path = prefix_path;
        if( path ){
            model_path += path + "/";
        }
        if (table) {
            var reg = new RegExp( '-|\_' , "g" );
            table = table.replace(reg," ");
            table = this.firstUpperCase(table);
            reg = new RegExp( ' ' , "g" );
            model_path += table.replace(reg,"") + ".py"
        }
        $(".gii_model_wrap .preview_path").html(model_path);
    },
    firstUpperCase: function (str) {
        var strArr = str.split(' ');
        for (var i = 0; i < strArr.length; i++) {
            strArr[i] = strArr[i].substring(0, 1).toUpperCase() + strArr[i].toLowerCase().substring(1)
        }
        return strArr.join(' ');
    }
};

$(document).ready(function () {
    gii_model_ops.init();
});