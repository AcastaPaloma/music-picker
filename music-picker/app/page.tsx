"use client"

import React, { useEffect } from 'react'

/// ========== Firebase ========== //
import { app, provider } from '@/lib/firebase'
import { getAuth, GoogleAuthProvider, signInWithPopup } from 'firebase/auth'

/// ========== Form Zod ========== //
import { z } from "zod"
import useUser from '@/lib/useUser'
import { useRouter } from 'next/navigation'


const Landing = () => {
  const auth = getAuth(app);
  const router = useRouter();
  const { user, loading } = useUser();

  useEffect(() => {
    if (!auth) return;
    if (!loading && !user) {
      router.push("/login");
    }
  }, [auth, user, loading, router]);
  
  return (
      <main>
        
      </main>
  )
}

export default Landing