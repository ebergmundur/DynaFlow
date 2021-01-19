
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
    path: '/about',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/About') }
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
      requiresLogged: false
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
      requiresLogged: false
    }
  },
  {
    path: '/testreal',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'testreal', component: () => import('pages/Realtestpage') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/testpractice',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'testpractice', component: () => import('pages/Testpage') }
    ],
    meta: {
      requiresLogged: false
    }
  },

  // {
  //   path: '/review',
  //   props: { exam: 1 },
  //   component: () => import('layouts/MainLayout.vue'),
  //   children: [
  //     { path: '', name: 'review', component: () => import('pages/Review') }
  //   ],
  //   meta: {
  //     requiresLogged: false
  //   }
  // },

  {
    path: '/review',
    props: { exam: 1 },
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/review/:id', name: 'review', component: (id) => import('pages/Review') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/flipcard',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'flipcard', component: () => import('pages/Flipcard') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/dashboard',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'dashboard', component: () => import('pages/Dashboard') }
    ],
    meta: {
      requiresLogged: false
    }
  },
  {
    path: '/userinfo',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'userinfo', component: () => import('pages/User') }
    ],
    meta: {
      requiresLogged: false
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
