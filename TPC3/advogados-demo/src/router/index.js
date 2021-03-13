import Vue from "vue";
import VueRouter from "vue-router";
import IndexView from "../views/IndexView.vue";
import RepoView from "@/views/RepoView"
import ClassView from "@/views/ClassView"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Index",
    component: IndexView
  },
  {
    path: "/repo/:repo_id/class/:class",
    name: "Class",
    component: ClassView
  },
  {
    path: "/repo/:repo_id",
    name: "Repo",
    component: RepoView
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
