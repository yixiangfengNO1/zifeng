<template>
  <div class="title">
    <span :class="{active:user.login_type==0}" @click="user.login_type=0">密码登录</span>
    <span :class="{active:user.login_type==1}" @click="user.login_type=1">短信登录</span>
  </div>
  <div class="inp" v-if="user.login_type==0">
    <input v-model="user.account" type="text" placeholder="用户名 / 手机号码 / 邮箱" class="user">
    <input v-model="user.password" type="password" class="pwd" placeholder="密码">
    <div id="geetest1"></div>
    <div class="rember">
      <label>
        <input type="checkbox" class="no" name="a"/>
        <span>记住密码</span>
      </label>
      <p>忘记密码</p>
    </div>
    <button class="login_btn" @click="show_captcha">登录</button>
    <p class="go_login">没有账号 <span>立即注册</span></p>
  </div>
  <div class="inp" v-show="user.login_type==1">
    <input v-model="user.mobile" type="text" placeholder="手机号码" class="user">
    <input v-model="user.code" type="text" class="code" placeholder="短信验证码">
    <el-button id="get_code" type="primary">获取验证码</el-button>
    <button class="login_btn">登录</button>
    <p class="go_login" >没有账号 <router-link to="/register">立即注册</router-link></p>
  </div>
</template>

<script setup>
import {reactive,watch} from "vue";
import user from "../api/user";
import {ElMessage} from 'element-plus'
import "../utils/TCaptcha"
const emit = defineEmits(["successhandle",])
import settings from "../settings";
import {useStore} from "vuex"
const store = useStore()

// 显示验证码
const show_captcha = ()=>{
  var captcha1 = new TencentCaptcha(settings.captcha_app_id, (res)=>{
    // 接收验证结果的回调函数
    /* res（验证成功） = {ret: 0, ticket: "String", randstr: "String"}
       res（客户端出现异常错误 仍返回可用票据） = {ret: 0, ticket: "String", randstr: "String", errorCode: Number, errorMessage: "String"}
       res（用户主动关闭验证码）= {ret: 2}
    */
    console.log(1111, res);
    // 调用登录处理
    loginhandler(res);
  });
  captcha1.show(); // 显示验证码
}

// 登录处理
const loginhandler = (res) => {
  // 验证数据
  if (user.account.length < 1 || user.password.length < 1) {
    // 错误提示
    //console.log(user.account)
    //console.log(user.password)
    //console.log("错了哦，用户名或密码不能为空！");
    ElMessage.error("错了哦，用户名或密码不能为空！");
    return;
  }

  // 登录请求处理
  user.login({
    ticket: res.ticket,
    randstr: res.randstr,
  }).then(response => {
    // 保存token，并根据用户的选择，是否记住密码
    localStorage.removeItem("token");
    sessionStorage.removeItem("token");
    console.log(response.data.token);
    if (user.remember) { // 判断是否记住登录状态
      // 记住登录
      localStorage.token = response.data.token
    } else {
      // 不记住登录，关闭浏览器以后就删除状态
      sessionStorage.token = response.data.token;
    }
    // 保存token，并根据用户的选择，是否记住密码
    // 成功提示
    ElMessage.success("登录成功！");
    console.log("登录成功！");
    // 关闭登录弹窗，对外发送一个登录成功的信息
    user.account = ""
    user.password = ""
    user.mobile = ""
    user.code = ""
    user.remember = false

    // vuex存储用户登录信息，保存token，并根据用户的选择，是否记住密码
    let payload = response.data.token.split(".")[1]  // 载荷
    let payload_data = JSON.parse(atob(payload)) // 用户信息
    console.log(payload_data)
    store.commit("login", payload_data)
    store.commit("cart_total", response.data.cart_total)
    emit("successhandle")
  }).catch(error => {
    ElMessage.error("登录失败！");
  })
}

const state = reactive({
  login_type: 0,
  username: "",
  password: "",
})

watch(() => state.mobile, (mobile, prevMobile) => {
  if(/1[3-9]\d{9}/.test(state.mobile)){
    // 发送ajax验证手机号是否已经注册

  }
})

</script>

<style scoped>
.title {
  font-size: 20px;
  color: #9b9b9b;
  letter-spacing: .32px;
  border-bottom: 1px solid #e6e6e6;
  display: flex;
  justify-content: space-around;
  padding: 0px 60px 0 60px;
  margin-bottom: 20px;
  cursor: pointer;
}

.title span.active {
  color: #4a4a4a;
  border-bottom: 2px solid #84cc39;
}

.inp {
  width: 350px;
  margin: 0 auto;
}

.inp .code {
  width: 220px;
  margin-right: 16px;
}

#get_code {
  margin-top: 6px;
}

.inp input {
  outline: 0;
  width: 100%;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
}

.inp input.user {
  margin-bottom: 16px;
}

.inp .rember {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  margin-top: 10px;
}

.inp .rember p:first-of-type {
  font-size: 12px;
  color: #4a4a4a;
  letter-spacing: .19px;
  margin-left: 22px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  /*position: relative;*/
}

.inp .rember p:nth-of-type(2) {
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .19px;
  cursor: pointer;
}

.inp .rember input {
  outline: 0;
  width: 30px;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
  vertical-align: middle;
  margin-right: 4px;
}

.inp .rember p span {
  display: inline-block;
  font-size: 12px;
  width: 100px;
}

.login_btn {
  cursor: pointer;
  width: 100%;
  height: 45px;
  background: #84cc39;
  border-radius: 5px;
  font-size: 16px;
  color: #fff;
  letter-spacing: .26px;
  margin-top: 30px;
  border: none;
  outline: none;
}

.inp .go_login {
  text-align: center;
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .26px;
  padding-top: 20px;
}

.inp .go_login span {
  color: #84cc39;
  cursor: pointer;
}
</style>