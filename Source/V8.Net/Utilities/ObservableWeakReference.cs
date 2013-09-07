﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

namespace V8.Net
{
    /// <summary>
    /// Notifies handlers that an object is ready to be garbage collected.
    /// To use this you must 1. wrap it in your class and pass it your class reference, 2. override the finalize method for your class and call "Finalize"
    /// on this weak reference object, and 3. keep a strong reference to this weak reference object so you can check it later (if needed).
    /// <para>Warning: This event is triggered in the GC thread!</para>
    /// </summary>
    /// <typeparam name="T">The object type to keep a reference for.</typeparam>
    public sealed class ObservableWeakReference<T> where T : class
    {
        /// <summary>
        /// Triggered when the GC wants to collect the object.
        /// </summary>
        public event Action<ObservableWeakReference<T>, T> GCReady;

        /// <summary>
        /// Set to true when the GC wants to collect the object.
        /// </summary>
        public bool IsGCReady { get { return _IsGCReady; } }
        volatile bool _IsGCReady;

        /// <summary>
        /// This is false by default, which prevents the object from being finalized in the garbage collection process.
        /// If you set this to true in an event handler, then upon return the object will continue being finalized.
        /// </summary>
        public bool CanCollect { get; set; }

        /// <summary>
        /// Returns a reference to the object wrapped by this instance.
        /// This is a weak reference at first, but will return the strong reference when the object is being finalized.
        /// <para>Note: The finalizer clears all weak references before running finalizers on all the objects, which means it's possible that main thread
        /// code may attempt to read this property, which would end up being 'null'.  However, this would be invalid, due to the fact 'DoFinalize()' hasn't been
        /// called yet.  To prevent this, this property is blocking if the target is set to null by the finalizer, until the finalizer triggers a call to
        /// 'DoFinalize()'.  As such, this property never returns 'null'.</para>
        /// </summary>
        public T Object { get { T o; while ((o = (T)_ObjectRef.Target ?? NearDeathReference) == null) Thread.Sleep(0); return o; } }

        WeakReference _ObjectRef;

        /// <summary>
        /// If 'IsGCReady' returns true, then this is the only reference that is keeping the object alive.
        /// </summary>
        public T NearDeathReference { get; private set; }

        /// <summary>
        /// Returns true if an attempt was made to garbage collect the object (see <see cref="NearDeathReference"/>).
        /// </summary>
        public bool IsNearDeathReference { get { return NearDeathReference != null; } }

        public ObservableWeakReference(T obj) { _ObjectRef = new WeakReference(obj); }

        public void DoFinalize(T obj)
        {
            NearDeathReference = obj;
            _IsGCReady = true;
            if (GCReady != null)
                GCReady(this, obj);
            if (!CanCollect) GC.ReRegisterForFinalize(obj);
        }

        public void SetTarget(T obj) { _ObjectRef.Target = obj; }

        /// <summary>
        /// If 'IsGCReady' is true, then this moves the near death reference back into the weak reference. If not, this method does nothing.
        /// <para>In either case, the underlying object is returned.</para>
        /// </summary>
        public T Reset()
        {
            var obj = Object; // (this is read first to cause blocking if the finalizer is working on the target object)
            if (_IsGCReady && NearDeathReference != null)
            {
                obj = NearDeathReference;
                SetTarget(obj);
                NearDeathReference = null;
            }
            return obj;
        }
    }
}
