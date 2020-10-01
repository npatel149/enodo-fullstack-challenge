import Vue from 'vue'
import VueRouter from 'vue-router'
import NProgress from 'nprogress';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "about" */ '../pages/PageHome.vue')
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../pages/PageAbout.vue')
  },
  {
    path: '/property',
    name: 'PropertyList',
    component: () => import(/* webpackChunkName: "property-list" */ '../pages/PagePropertyList.vue'),
  },
  {
    path: '/property/:id',
    name: 'PropertyListDetail',
    props: true,
    component: () => import(
      /* webpackChunkName: "property-details" */ '../pages/PagePropertyListDetail.vue'
      ),
  },
  {
    path: '/property-selected/',
    name: 'PropertyListTable',
    component: () => import(/* webpackChunkName: "property-list-table" */ '../pages/PagePropertyListTable.vue')
  },
  {
    path: '/404',
    alias: '*',
    name: 'NotFound',
    component: () => import(/* webpackChunkName: "not-found" */'../pages/PageNotFound.vue'),
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  NProgress.start();
  console.log(`🚦 navigating to ${to.name} from ${from.name} and next ${next.name}`);
  next();
});

router.afterEach(() => {
  NProgress.done();
});

export default router
