import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import TriangleArea from "@/components/TriangleArea.vue";
import MaxEdge from "@/components/MaxEdge.vue";
import Conversion from "@/components/Conversion.vue";
import Recurse from "@/components/Recurse.vue";
import BodyGreeting from "@/components/BodyGreeting.vue";
import Body from "@/components/Body.vue";
import Header from "@/components/Header.vue";
import FAQ from "@/views/FAQ.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    children: [
      {
        path: "faq",
        component: FAQ
      },
      {
        path: "body",
        name: "body",
        component: Body,
        children: [
          {
            path: "bodygreeting",
            name: "bodygreeting",
            component: BodyGreeting
          },
          {
            path: "trianglearea",
            name: "trianglearea",
            component: TriangleArea
          },
          {
            path: "maxedge",
            name: "maxedge",
            component: MaxEdge
          },
          {
            path: "conversion",
            name: "conversion",
            component: Conversion
          },
          {
            path: "recurse",
            name: "recurse",
            component: Recurse
          }
        ]
      }
    ]
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
