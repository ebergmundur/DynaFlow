
const routes = [
  // {
  //   path: '/',
  //   component: () => import('src/App.vue')
  // },
  {
    path: '/',
    component: () => import('src/layouts/MainLayout'),
    children: [
      { path: '', name: 'home', component: () => import('pages/Index.vue') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/question',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Question.vue') }
    ],
    meta: {
      requiresLogged: true
    }
  },
  // {
  //   path: '/collect',
  //   component: () => import('layouts/MainLayout.vue'),
  //   children: [
  //     { path: '', component: () => import('components/CollectQuestions.vue') }
  //   ],
  //   meta: {
  //     requiresLogged: false
  //   }
  // },

  {
    path: '/createtest',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/CreatePractice.vue') }
    ],
    meta: {
      requiresLogged: true
    }
  },
  {
    path: '/testreal',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Testpage') }
    ],
    meta: {
      requiresLogged: true
    }
  },
  {
    path: '/testpractice',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'testpractice', component: () => import('pages/Testpage') }
    ],
    meta: {
      requiresLogged: true
    }
  },
  {
    path: '/review',
    props: { exam: 1 },
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'review', component: () => import('pages/Review') }
    ],
    meta: {
      requiresLogged: true
    }
  },
  {
    path: '/flipcard',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'flipcard', component: () => import('pages/Flipcard') }
    ],
    meta: {
      requiresLogged: true
    }
  },
  {
    path: '/dashboard',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'dashboard', component: () => import('pages/Dashboard') }
    ],
    meta: {
      requiresLogged: true
    }
  },
  {
    path: '/userinfo',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'userinfo', component: () => import('pages/User') }
    ],
    meta: {
      requiresLogged: true
    }
  },
  {
    path: '/login',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'login', component: () => import('pages/Login') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/register',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'register', component: () => import('pages/Register') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/logout',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'logout', component: () => import('pages/Logout') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  // {
  //   path: '/callback',
  //   component: () => import('layouts/MainLayout.vue'),
  //   children: [
  //     { path: '', component: () => import('components/Clock') }
  //   ]
  // },
  // {
  //   path: '/callback',
  //   component: () => import('layouts/MainLayout.vue'),
  //   children: [
  //     { path: '', name: 'downloads', component: () => import('components/Dashboard') }
  //   ]
  // },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue'),
    meta: {
      requiresLogged: false
    }
  }
]

export default routes
